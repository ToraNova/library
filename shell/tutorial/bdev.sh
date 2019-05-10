#begin devlopment script
#similar to dev2.sh but starts with b so easier to launc

#open python files only
find . -regextype posix-egrep -regex ".*\.(py)$" -exec notepadqq {} +
