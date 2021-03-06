### Hello World PBS Submission Script

#!/bin/sh

### Job name
#PBS -N hello_world_job

### Output files
#PBS -o hello_world_job.stdout
#PBS -e hello_world_job.stderr

### Queue name; disabled now
##PBS -q dqueue

### Number of nodes
#PBS -l nodes=1

## Print the default PBS server
echo PBS default server is $PBS_DEFAULT

## Print the job's working directory and enter it.
echo Working directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR

## Print some other environment information
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo This jobs runs on the following processors:
NODES=`cat $PBS_NODEFILE`
echo $NODES

## Compute the number of processors
NPROCS=`wc -l < $PBS_NODEFILE`
echo This job has allocated $NPROCS nodes

: <<'END'
## Run hello_world or any othr program
for NODE in $NODES; do
 ssh $NODE "hello_world" &
done

## Wait for background jobs to complete.
wait
END

##sleep to check functioning with qstat
sleep 5m
echo "BYE"
