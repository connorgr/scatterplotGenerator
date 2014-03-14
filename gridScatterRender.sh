FILES=/home/connor/scatterplotGenerator/out/*
for f in $FILES
do
  echo "svg${f//\//-}"
  ./submitScatterRender.sh "svg${f//\//-}" $f
done

#qsub -cwd -N "vizDataGenerator$c$m$s$slope$q$r" -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf /home/connor/scatterplotGenerator/gridReady.py $c $m $s $slope $q $r