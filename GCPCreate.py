from googleapiclient.discovery import build
import google

credentials, projectid = google.auth.default()
compute_engine = build('compute', 'v1', credentials=credentials)

# Need these parameters to create a server
  # Project ID for this request.
project = 'gcptest-299019'  # TODO: Update placeholder value.
  # The name of the zone for this request.
zone = 'us-central1-a'  # TODO: Update placeholder value.
  # Name of there virtual server
name = 'swingsvm' # TODO: Change the name
  # Server size
machine_type = 'e2-micro' # TODO: Set the type of server


config = {
  "name": "swingsvm",
  "machineType": "projects/gcptest-299019/zones/us-central1-a/machineTypes/f1-micro",
  "displayDevice": {
    "enableDisplay": False
  },
  "disks": [
    {
      "kind": "compute#attachedDisk",
      "type": "PERSISTENT",
      "boot": True,
      "mode": "READ_WRITE",
      "autoDelete": True,
      "deviceName": "swingsvm",
      "initializeParams": {
        "sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20201112",
        "diskType": "zones/us-central1-a/diskTypes/pd-standard",
        "diskSizeGb": "10",
        "labels": {}
      },
      "diskEncryptionKey": {}
    }
  ],
  "canIpForward": False,
  "networkInterfaces": [
    {
      "kind": "compute#networkInterface",
      "subnetwork": "regions/us-central1/subnetworks/default",
      "accessConfigs": [
        {
          "kind": "compute#accessConfig",
          "name": "External NAT",
          "type": "ONE_TO_ONE_NAT",
          "networkTier": "STANDARD" # TODO: changed this from PREMIUM to STANDARD
        }
      ],
      "aliasIpRanges": []
    }
  ]
}

request = compute_engine.instances().insert(project=project, zone=zone, body=config)
response = request.execute()

print('hello')