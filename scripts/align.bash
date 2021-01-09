# Aln Procedures
sudo docker run -v '/home/dm/aula6_7/dados/:/data' -it biocontainers/bwa:v0.7.17-3-deb_cv1 bash
cd /data

bwa index Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz

bwa aln Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4157959_1P.fastq.gz > ERR4157959_1P.sai
bwa aln Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4157959_2P.fastq.gz > ERR4157959_2P.sai
bwa aln Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4395294_1P.fastq.gz > ERR4395294_1P.sai
bwa aln Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4395294_2P.fastq.gz > ERR4395294_2P.sai

# shorter aln files than just one seq
bwa sampe -f ERR4157959.aln.sam Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4157959_1P.sai ERR4157959_2P.sai ERR4157959_1P.fastq.gz ERR4157959_2P.fastq.gz
bwa sampe -f ERR4395294.aln.sam Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz ERR4395294_1P.sai ERR4395294_2P.sai ERR4395294_1P.fastq.gz ERR4395294_2P.fastq.gz

exit

# Aln cleaning
sudo docker run -v /home/dm/aula6_7/dados/:/data -it biocontainers/samtools:v1.7.0_cv4 bash
cd /data

samtools view -Sb ERR4157959.aln.sam > ERR4157959.aln.bam
samtools view -Sb ERR4395294.aln.sam > ERR4395294.aln.bam
samtools sort ERR4157959.aln.bam -o ERR4157959.aln.sort.bam
samtools sort ERR4395294.aln.bam -o ERR4395294.aln.sort.bam
samtools index ERR4157959.aln.sort.bam
samtools index ERR4395294.aln.sort.bam
samtools flagstat ERR4157959.aln.sort.bam > ERR4157959_aln_stats
samtools flagstat ERR4395294.aln.sort.bam > ERR4395294_aln_stats
cat ERR4157959_aln_stats
cat ERR4395294_aln_stats

# Stats

biodocker@fe5fa6172a9a:/data$ cat ERR4157959_aln_stats
2102124 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
2089210 + 0 mapped (99.39% : N/A)
2102124 + 0 paired in sequencing
1051062 + 0 read1
1051062 + 0 read2
1298094 + 0 properly paired (61.75% : N/A)
2083536 + 0 with itself and mate mapped
5674 + 0 singletons (0.27% : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)

biodocker@fe5fa6172a9a:/data$ cat ERR4395294_aln_stats
34254 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
33402 + 0 mapped (97.51% : N/A)
34254 + 0 paired in sequencing
17127 + 0 read1
17127 + 0 read2
27376 + 0 properly paired (79.92% : N/A)
32972 + 0 with itself and mate mapped
430 + 0 singletons (1.26% : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)

# Verificar Alinhamentos

samtools tview ERR*.aln.sort.bam Sars_cov_2.ASM985889v3.dna.toplevel.fa.gz

# BCFTOOLS
sudo docker run -v /home/dm/aula6_7/dados:/data -it quay.io/biocontainers/bcftools:1.9--h68d8f2e_7 bash
cd /data

#Identificar  os  variantes  eextrair para um ficheiro vcf
bcftools mpileup -Ou -f Sars_cov_2.ASM985889v3.dna.toplevel.fa ERR4157959.aln.sort.bam | bcftools call -Ov -vc > ERR4157959.sars_cov.raw.vcf
bcftools mpileup -Ou -f Sars_cov_2.ASM985889v3.dna.toplevel.fa ERR4395294.aln.sort.bam | bcftools call -Ov -vc > ERR4395294.sars_cov.raw.vcf