"""
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

# import boto3
import requests
import os
import json
KEYSERVER_URL = os.environ["KEYSERVER_URL"]


class KeyCache:
    """
    This class is responsible for storing keys in the key cache (S3) and
    returning a URL that can return a specific key from the cache.
    """

    def __init__(self, keystore_bucket, client_url_prefix):
        self.keystore_bucket = keystore_bucket
        self.client_url_prefix = client_url_prefix

    def retrieve(self, content_id, key_id):
        """
        Store a key into the cache (S3) using the content_id
        as a folder and key_id as the file
        """
        # Get from DRM server
        response = requests.get(
            url=KEYSERVER_URL,
            params={"contentId":content_id,"keyId":key_id}
        )
        return json.loads(response.text)

    def store(self, content_id, key_id, key_value):
        """
        Store a key into the cache (S3) using the content_id
        as a folder and key_id as the file
        """
        # key = "{cid}/{kid}".format(cid=content_id, kid=key_id)
        # s3_client = boto3.client('s3')
        # store the key file with public-read permissions
        # public bucket policy not required
        # s3_client.put_object(Bucket=self.keystore_bucket, Key=key, Body=key_value)
        request_data = {"AssetID":content_id,"KeyHEX":key_value.hex(),"KeyID":key_id}
        # Send to DRM server
        requests.post(
            url=KEYSERVER_URL+"/insert",
            json=request_data
        )

    def url(self, content_id, key_id):
        """
        Return a URL that can be used to retrieve the
        specified key_id related to content_id
        """
        return "{}/{}/{}".format(self.client_url_prefix, content_id, key_id)
