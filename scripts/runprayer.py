# import sys
# from prayertrack import prayer_tracking
# # from mygrpcapp import bible_service
# import django.conf

# try:
#     django.conf.settings.configure('C:\\Users\\HP\Desktop\\BibleApp\\settings.py')
# except AttributeError:
#     print('Something went wrong while configuring the Django settings module.')
#     print('Please make sure that you have configured the Django settings module before running this script.')
#     exit(1)
import sys
from mygrpcapp import bible_service

# The rest of your code goes here.


if __name__ == '__main__':
    # sys.path.append('C:\\Users\\HP\\Desktop\\shadow')
    # sys.path.append(r'C:\\Users\\HP\Desktop\\shadow\\mygrpcapp')
    # prayer_tracking.serve() 
    bible_service.grpc_serve() 



# import subprocess
# import os
# # Get the current directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# # Set the current working directory to the Django project's root directory
# os.chdir(current_dir)

# # Define a list of server scripts to start
# server_scripts = [
#     'mygrpcapp\\bible_service.py',
#     'prayertrack\\prayer_tracking.py',
#     # 'prayertrack\\management\\commands\\prayer_tracking.py',
#     # 'mygrpcapp\\management\\commands\\bible_service.py',
#     # 'app3/server_script3.py',
#     # Add more server scripts as needed
# ]

# # Iterate through the list and start each server script
# for script in server_scripts:
#     command = f'python {script}'
#     subprocess.Popen(command, shell=True)
