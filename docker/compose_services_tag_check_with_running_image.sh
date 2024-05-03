#!/bin/bash
# It extracts a list of service names from a Docker Compose file, and checks if each service is running the latest image tag specified in the Docker Compose file, displaying the comparison between the specified tag and the running container tag.
# Path to the Docker Compose file
COMPOSE_FILE="/var/home/docker-user/autodeploy/Bansira-SuperApp.Microservices/utils/deploy/docker-compose.yaml"

cd "$(dirname "$COMPOSE_FILE")" || exit
#pull_output=$(git pull)
#echo "$pull_output"

# Get a list of service names
awk '/^[[:space:]]*[^#]*:$/{sub(/:/,""); gsub(/[[:space:]]*/, ""); print}' $COMPOSE_FILE > /tmp/service_list.txt
sed -i -e '1,/^services$/d; /^services$/d; s/ports//g; s/networks//g; s/labels//g; s/environment//g' -e '/^$/d' /tmp/service_list.txt

# Get a list of tags
imagetags_list=$(cat $COMPOSE_FILE | grep -E "^ *image:.*" | awk -F':' '{print $3}')

check_service_tag() {
    service=$1
    image_tag=$2
    running_image=$(docker inspect --format='{{index .Config.Image}}' $service 2>/dev/null)
    running_tag=$(echo "$running_image" | awk -F':' '{print $2}')
    if [[ "$image_tag" == "$running_tag" ]]
    then
        printf "OK - %-25s Already updated with Tag:%-15s \n" "$service" "$image_tag"
    else
        printf "NO - %-25s is old | Latest Tag is: %-15s \n" "$service" "$image_tag"
    fi
}

while read -r service; do
    read -r image_tag <&3
    check_service_tag $service $image_tag
done < /tmp/service_list.txt 3< <(echo "$imagetags_list")

echo "Script execution completed."
