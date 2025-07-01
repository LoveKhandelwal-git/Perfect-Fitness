import requests
import json

# The base URL of your Flask application
base_url = "http://127.0.0.1:5000" 

poses_data = [
    {
        "pose_name": "Chair",
        "pose_image": "https://pocketyoga.com/assets/images/full/Chair.png",
        "pose_link": "https://www.youtube.com/watch?v=tEZhXr0FuAQ&pp=ygUTY2hhaXIgcG9zZSB0dXRvcmlhbA%3D%3D"
    },
    {
        "pose_name": "Cobra",
        "pose_image": "https://pocketyoga.com/assets/images/full/CobraFull.png",
        "pose_link": "https://www.youtube.com/watch?v=zgvolE4NAH0&pp=ygUTY29icmEgcG9zZSB0dXRvcmlhbA%3D%3D"
    },
    {
        "pose_name": "Dog",
        "pose_image": "https://pocketyoga.com/assets/images/full/Dolphin.png",
        "pose_link": "https://www.youtube.com/watch?v=ayQoxw8sRTk&pp=ygURZG93bndhcmQgZG9nIHBvc2U%3D"
    },
    {
        "pose_name": "Goddess",
        "pose_image": "https://pocketyoga.com/assets/images/full/Goddess_R.png",
        "pose_link": "https://www.youtube.com/watch?v=cekN3sdUNso&pp=ygUMZ29kZGVzcyBwb3Nl"
    },
    {
        "pose_name": "Mountain",
        "pose_image": "https://pocketyoga.com/assets/images/full/MountainArmsSide.png",
        "pose_link": "https://www.youtube.com/watch?v=5NxDs-ovJU8&pp=ygUNbW91bnRhaW4gcG9zZQ%3D%3D"
    },
    {
        "pose_name": "Plank",
        "pose_image": "https://pocketyoga.com/assets/images/full/Plank.png",
        "pose_link": "https://www.youtube.com/watch?v=pvIjsG5Svck&pp=ygUKcGxhbnQgcG9zZQ%3D%3D"
    },
    {
        "pose_name": "Tree",
        "pose_image": "https://pocketyoga.com/assets/images/full/TreePrayer_L.png",
        "pose_link": "https://www.youtube.com/watch?v=uELr6MPi7pI&pp=ygUJdHJlZSBwb3Nl"
    },
    {
        "pose_name": "Triangle",
        "pose_image": "https://pocketyoga.com/assets/images/full/FallenTriangle_L.png",
        "pose_link": "https://www.youtube.com/watch?v=S6gB0QHbWFE&pp=ygUNdHJpYW5nbGUgcG9zZQ%3D%3D"
    },
    {
        "pose_name": "Warrior",
        "pose_image": "https://pocketyoga.com/assets/images/full/WarriorIII_L.png",
        "pose_link": "https://www.youtube.com/watch?v=uEc5hrgIYx4&pp=ygUOd2FycmlvciAzIHBvc2U%3D"
    },
    {
        "pose_name": "Warrior2",
        "pose_image": "https://pocketyoga.com/assets/images/full/WarriorII_L.png",
        "pose_link": "https://www.youtube.com/watch?v=Mn6RSIRCV3w&pp=ygUOd2FycmlvciAyIHBvc2XSBwkJhgkBhyohjO8%3D"
    },
    {
        "pose_name": "Sitting",
        "pose_image": "https://pocketyoga.com/assets/images/full/Easy.png",
        "pose_link": "https://www.youtube.com/watch?v=ngi5pWhOTZc&pp=ygUNU3VraGFzYW5heW9nYQ%3D%3D"
    },
    {
        "pose_name": "King dancer",
        "pose_image": "https://insideyoga.org/wp-content/uploads/2024/03/50_Natarajasana.jpg",
        "pose_link": "https://www.youtube.com/watch?v=TXNgRNsqcPo&pp=ygUQa2luZyBkYW5jZXIgcHNvZQ%3D%3D"
    }
]

def add_pose_to_db(pose_data):
    """Sends a POST request to add a pose to the database."""
    url = f"{base_url}/poses"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, data=json.dumps(pose_data), headers=headers)
        if response.status_code == 201:
            print(f"Successfully added pose: {pose_data['pose_name']}")
            print("Response:", response.json())
        elif response.status_code == 409:
            print(f"Pose already exists: {pose_data['pose_name']}")
            print("Response:", response.json())
        else:
            print(f"Failed to add pose: {pose_data['pose_name']}")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the server for pose {pose_data['pose_name']}: {e}")
    print("-" * 30)

if __name__ == "__main__":
    for pose in poses_data:
        add_pose_to_db(pose)