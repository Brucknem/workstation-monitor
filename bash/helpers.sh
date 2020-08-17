function join()
{
    path=$1
    if [[ ! "$path" == "*/" ]]
    then
        path+="/"
    fi
    [ -d $path ] || mkdir $path
    echo $path$2
}
export -f join