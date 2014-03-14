NAME=$1
FILE=$2
echo $NAME
echo $FILE
qsub -cwd -N $NAME -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf /home/connor/scatterplotGenerator/gridRenderScatter.js --outdir=/home/connor/scatterplotGenerator/svg --json=$FILE