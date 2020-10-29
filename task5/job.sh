#!/bin/bash

#*********************************************************************#
# Antes de executar ./job.sh você deve dar perminsão para o arquivo   #
# possa ser executado. Para isso, execute o seginte comando:          #
#              chmod +x job.sh                                        #
#*********************************************************************#

echo
echo start: $(date "+%d/%m/%y %H:%M:%S.%3N")
echo

numeroExecucoes=30

tamanhoVetor="100 1000 10000 100000 1000000 10000000 100000000 1000000000"
# tamanhoVetor="100 1000 10000"

numThreads="1 6 12 18 24"

for N in $tamanhoVetor
do
	echo "------------------------------------------------"
	echo "N = "$N
	echo "------------------------------------------------"
	for T in $numThreads
	do
		echo "Threads = "$T
		for (( i=1; i<numeroExecucoes; i++ ))
		do
			./pratica $T $N 
		done
		echo
	done
	echo
done

echo
echo stop:  $(date "+%d/%m/%y %H:%M:%S.%3N")
echo