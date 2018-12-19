

class GenomeUrl(object):
    """A class to hold url for genomes and possible gff files and with a unique identifier, class will be used to download and store genomes as genome_id.

    :param genome_url: The url for the genome.
    :param genome_id: a unique identifier for the genome
    :param genome_type: The type of genome, should be chromosome or scaffold.
    :param gff_url: If a gff3 file is available the url for this file.
    :param genome_version: if there is a version for the genome
    """
    def __init__(self, genome_url, genome_id, genome_type, gff_url = "", genome_version = "v1"):
      self.genome_url = genome_url
      self.id = genome_id
      self.type = genome_type
      self.gff_url = gff_url
      self.version = genome_version

