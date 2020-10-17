if [ -d "created_dir" ]; then
  rm -rf created_dir
fi


mkdir created_dir
cd created_dir
for i in {1..100}
do

mkdir DDM$i
cd DDM$i
echo nanoseconds since 1970-01-01 00:00:00 UTC: >> time_till_now.txt
echo $(( $(date '+%s%N') )) >>time_till_now.txt
cd ..
done
