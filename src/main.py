import subprocess

scripts = [
    'src/channel_details_raw.py',
    'src/channel_details_stage.py',
    'src/video_header_raw.py',
    'src/video_header_stage.py',
    'src/video_details_raw.py',
    'src/video_details_stage.py',
    'src/comment_details_raw.py',
    # 'src/comment_details_stage.py'
    ]



for script in scripts:
    print(f'Running {script}...')
    result = subprocess.run(['python', script], capture_output=True, text=True)
    print(f'--- Output of {script} ---')
    print(result.stdout)
    if result.stderr:
        print(f'--- Errors in {script} ---')
        print(result.stderr)


