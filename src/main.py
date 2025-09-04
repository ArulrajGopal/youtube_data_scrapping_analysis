import subprocess

scripts = [
    # 'src/cleanup.py',
    # 'src/load_channel_details_raw.py',
    # 'src/load_channel_details_stage.py',
    'src/load_video_header_raw.py',
    # 'src/load_video_header_stage.py',
    # 'src/load_video_details_raw.py',
    # 'src/load_video_details_stage.py',
    # 'src/load_comment_details_raw.py',
    # 'src/load_comment_details_stage.py'
    ]


for script in scripts:
    print(f"\nRunning {script}...")
    process = subprocess.Popen(
        ['python', script],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    # Print logs in real-time
    for line in process.stdout:
        print(line, end='')

    process.wait()  # Wait for script to finish

    if process.returncode == 0:
        print(f"\n{script} completed successfully.")
    else:
        print(f"\n{script} failed with exit code {process.returncode}.")

