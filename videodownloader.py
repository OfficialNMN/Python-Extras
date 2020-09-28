url='https://cdnhls.nichevid.com/4/4/8/5/7/d5a7aef0-e66d-4b06-9182-479a20da1e7c_partintroduction-1M.m3u8'

import m3u8
import requests

r=requests.get(url)

m3u8_master=m3u8.loads(r.text)

print(m3u8_master.data)

# m3u8_master.data['segments'][0]['uri']

# m3u8_master.data['segments'][1]['uri']

r=requests.get('https://cdnhls.nichevid.com/4/4/8/5/7/'+m3u8_master.data['segments'][0]['uri'])

# r.content

with open('video.ts','wb') as f:
	f.write(r.content)

# with open("fullvideo.ts", 'wb') as f:
#     for segment in m3u8_master.data['segments']:
#         url=segment['uri']
#         r = requests.get('https://cdnhls.nichevid.com/4/4/8/5/7/'+url)
#         f.write(r.content)

# import subprocess
# subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])

