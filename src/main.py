import subprocess

scripts = [
    'src/cleanup.py',
    # 'src/load_channel_details_raw.py',
    # 'src/load_channel_details_stage.py',
    # 'src/load_video_header_raw.py',
    # 'src/load_video_header_stage.py',
    # 'src/load_video_details_raw.py',
    # 'src/load_video_details_stage.py'
    'src/load_comment_details_raw.py',
    'src/load_comment_details_stage.py'
    ]



for script in scripts:
    print(f'Running {script}...')
    result = subprocess.run(['python', script], capture_output=True, text=True)
    print(f'--- Output of {script} ---')
    print(result.stdout)
    if result.stderr:
        print(f'--- Errors in {script} ---')
        print(result.stderr)


