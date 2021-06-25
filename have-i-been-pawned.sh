#!/bin/bash
mypws=('ucanttouchthis' 'iloveyou' 'monkey')
 
for mypw in "${mypws[@]}"
do
  echo "pw : $mypw"
  sha=`echo -n $mypw | sha1sum` 
  shapref="${sha:0:5}"  
  shasuff="${sha:5:20}"
  shasuffupper=${shasuff^^}
  curl https://api.pwnedpasswords.com/range/$shapref 2>/dev/null| grep $shasuffupper
done

