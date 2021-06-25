#!/bin/bash
echo "\
Usage :
. .\have-i-been-pawned.sh : test run with fake passwords
. .\have-i-been-pawned.sh pw1 'pw!2' 'pw\3' mypw : run with passwords passed in args
NB : enclose pw with special chars in single quotes !

"

mypws=( "$@" )

if [ $# -eq 0 ]; then
  mypws=('ucantto!uchthis' 'iloveyou' 'monkey')
fi
 
for mypw in "${mypws[@]}"
do
  echo "pw : $mypw"
  sha=`echo -n $mypw | sha1sum` 
  shapref="${sha:0:5}"  
  shasuff="${sha:5:20}"
  shasuffupper=${shasuff^^}
  curl https://api.pwnedpasswords.com/range/$shapref 2>/dev/null| grep $shasuffupper
done

