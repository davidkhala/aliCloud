set -e
configure(){
  local key=$1
  local secret=$2
  local region=${region:-"cn-hongkong"}
  aliyun configure set --profile default --mode AK --access-key-id $key --access-key-secret $secret --region $region
}
"$@"

