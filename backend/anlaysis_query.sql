-- This SQL query retrieves the most viewed video from each channel along with channel details.
select 
    C.title as channel,
    C.videocount,
    C.viewcount as total_views,
    A.title as video_title, 
    A.duration, 
    A.likecount, 
    A.view_count, 
    A.commentcount 
from video_details_stage A 
join 
(select 
    channel_id, 
    max(view_count) as view_count
from video_details_stage
group by channel_id
) B 
on A.channel_id = B.channel_id 
and A.view_count = B.view_count
join channel_details_stage C 
on A.channel_id = C.channel_id


-- datatype check query
SELECT 
    column_name, 
    data_type,
    character_maximum_length,
    numeric_precision,
    numeric_scale,
    is_nullable,
    column_default
FROM 
    information_schema.columns
WHERE 
    table_schema = 'public'  -- change if your table is in a different schema
    AND table_name = 'comment_details_stage';  -- replace with your actual table name
