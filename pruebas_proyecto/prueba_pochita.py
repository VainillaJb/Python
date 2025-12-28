import os

# Esta es la URL "mágica" que encontraste
url_directa = "https://v16-webapp-prime.tiktok.com/video/tos/maliva/tos-maliva-ve-0068c799-us/ocv5WEAzPBgYPwEnxViZQvMViRtPBcjVEV9IA/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=1018&bt=509&cs=2&ds=3&ft=I~da4od0D12Nv6juP.IxR8jSglJG-UjNSaopiX&mime_type=video_mp4&qs=14&rc=Zjw7ZzM4NzlkOWhpaTpkaEBpM2kzcGo5cjZ1dTMzaTczNEAyYWE0YGJjXjMxMF80Xl5jYSMzNTFrMmQ0b15gLS1kMTJzcw%3D%3D&btag=e000b8000&expire=1767023516&l=20251227235141CA23DC827CC3379D0596&ply_type=2&policy=2&signature=38f45e62905ad8badc5480b9b1dd9795&tk=tt_chain_token" 

# Usamos --app para que no haya barra de búsqueda
# Y forzamos el inicio automático por si acaso
os.system(f'start chrome --app="{url_directa}" --autoplay-policy=no-user-gesture-required')