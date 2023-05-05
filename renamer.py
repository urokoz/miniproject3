outfile = open("renamed_covid_genomes.fasta", "w")

with open("covid_genomes.fasta", "r") as f:
    for line in f:
        if line.startswith(">"):
            header = line.split("|")
            id = header[0].strip()
            country = header[3].strip().replace(" ", "_")
            date = header[4].strip().split("-")
            year = date[0]
            month = date[1]
            day = date[2]
            line = f"{id}_{country}_{year}/{month}/{day}\n"
        
        outfile.write(line)
outfile.close()