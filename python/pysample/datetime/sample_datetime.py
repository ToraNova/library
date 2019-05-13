import datetime

# I always forgot this freaking syntax
# thus, I am writing this down

format_string = "%Y/%m/%d %B %w (W/D:%W/%j) %A (%a) %H:%M:%S_%f %Z or %I%p"
dfstr = "%Y/%m/%d %a %H:%M:%S"
print( datetime.datetime.now().strftime(format_string) )
