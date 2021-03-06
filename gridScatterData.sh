# c = sys.argv[1] # color layout = ['grouped','random']
# m = sys.argv[2] # mark size = [4,6,8,10]
# s = sys.argv[3] # set size = [196, 324, 484]
# slope = sys.argv[4] # slope = ['positive', 'negative']
# q = sys.argv[5] # quadrant = ['tl', 'tr', 'bl', 'br']
# r = sys.argv[6] # repetition = 10

cd /home/connor/scatterplotGenerator

layouts=( "grouped" "random")
markSizes=( 4 6 8 10 )
setSizes=( 196 324 484 )
slopes=( "positive" "negative")
quads=("tl" "tr" "bl" "br")
reps=( 1 2 3 4 5 6 7 8 9 10 )

for c in "${layouts[@]}"
do
  for m in "${markSizes[@]}"
  do
    for s in "${setSizes[@]}"
    do
      for slope in "${slopes[@]}"
      do
        for q in "${quads[@]}"
        do
          for r in "${reps[@]}"
          do
            echo "----------------------------"
            # qsub -N vizDataGenerator -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf ./gridScatterData.sh
            # python /home/connor/scatterplotGenerator/gridDataFactory.py $c $m $s $slope $q $r
            qsub -cwd -N "vizDataGenerator$c$m$s$slope$q$r" -V -e /home/connor/scatterplotGenerator/gridOut -o /home/connor/scatterplotGenerator/gridOut -l inf /home/connor/scatterplotGenerator/gridReady.py $c $m $s $slope $q $r
          done
        done
      done
    done
  done
done
