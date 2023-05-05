outfile = open("covid_genomes_metadata.tsv", "w")
outfile.write("ID\tCountry\tYear\tMonth\tDay\n")
with open("covid_genomes.fasta", "r") as f:
    for line in f:
        if line.startswith(">"):
            header = line.split("|")
            id = header[0].strip().replace(">", "")
            country = header[3].strip()
            date = header[4].strip().split("-")
            year = date[0]
            month = date[1]
            day = date[2]
            metadata = f"{id}\t{country}\t{year}\t{month}\t{day}\n"
        
            outfile.write(metadata)
outfile.close()