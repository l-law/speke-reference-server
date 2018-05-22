"""
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from botocore.vendored import requests
import boto3
import json
import string
import random
import uuid
import resource_tools
import mediapackage_endpoint_common as common


def event_handler(event, context):
    """
    Lambda entry point. Print the event first.
    """
    print("Event Input: %s" % json.dumps(event))
    try:
        mediapackage = boto3.client('mediapackage')
        if event["RequestType"] == "Create":
            result = create_endpoint(mediapackage, event, context)
        elif event["RequestType"] == "Update":
            result = common.update_endpoint(
                mediapackage,  create_endpoint, event, context)
        elif event["RequestType"] == "Delete":
            result = common.delete_endpoint(mediapackage, event, context)
    except Exception as exp:
        print("Exception: %s" % exp)
        result = {
            'Status': 'FAILED',
            'Data': {"Exception": str(exp)},
            'ResourceId': None
        }
    resource_tools.send(event, context, result['Status'],
                        result['Data'], result['ResourceId'])
    return


def create_endpoint(mediapackage, event, context, auto_id=True):
    """
    Create a MediaPackage channel
    Return the channel URL, username and password generated by MediaPackage
    """

    if auto_id:
        endpoint_id = "%s-%s" % (resource_tools.stack_name(event), event["LogicalResourceId"])
    else:
        endpoint_id = event["PhysicalResourceId"]

    channel_id = event["ResourceProperties"]["ChannelId"]
    rotation_interval = event["ResourceProperties"]["RotationInterval"]
    role_arn = event["ResourceProperties"]["RoleArn"]
    server_url = event["ResourceProperties"]["ServerUrl"]

    try:
        response = mediapackage.create_origin_endpoint(
            Id=endpoint_id,
            Description="CloudFormation Stack ID %s" % event["StackId"],
            ChannelId=channel_id,
            ManifestName="index",
            StartoverWindowSeconds=0,
            HlsPackage={
                "SegmentDurationSeconds": 6,
                "PlaylistWindowSeconds": 60,
                "PlaylistType": "event",
                "AdMarkers": "none",
                "IncludeIframeOnlyStream": True,
                "UseAudioRenditionGroup": True,
                "StreamSelection": {
                    "StreamOrder": "original"
                },
                "Encryption": {
                    "EncryptionMethod": "AES_128",
                    "KeyRotationIntervalSeconds": int(rotation_interval),
                    "RepeatExtXKey": False,
                    "SpekeKeyProvider": {
                        "ResourceId": str(uuid.uuid4()),
                        "RoleArn": role_arn,
                        "SystemIds": [
                            "81376844-f976-481e-a84e-cc25d39b0b33"
                        ],
                        "Url": server_url
                    }
                }

            }
        )
        print(json.dumps(response))
        outputs = {
            "OriginEndpointUrl": response['Url']
        }
        result = {
            'Status': 'SUCCESS',
            'Data': outputs,
            'ResourceId': endpoint_id
        }

    except Exception as ex:
        print(ex)
        result = {
            'Status': 'FAILED',
            'Data': {"Exception": str(ex)},
            'ResourceId': endpoint_id
        }

    return result
