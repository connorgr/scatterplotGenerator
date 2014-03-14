FILES = /home/connor/scatterplotGenerator/gridOut/*
for f in $FILES
do
  qsub -cwd -N "svg$f" -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf node /home/connor/scatterplotGenerator/gridRenderScatter.js --outdir=/home/connor/scatterplotGenerator/svg --json=$f
done

#qsub -cwd -N "vizDataGenerator$c$m$s$slope$q$r" -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf /home/connor/scatterplotGenerator/gridReady.py $c $m $s $slope $q $r