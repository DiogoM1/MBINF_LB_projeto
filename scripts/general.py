from datetime import datetime


def time_stamping(file):
    """
    Small function that datetime stamps file names and outputs
    This method allows the processing of complex filenames like gene.vcf.tar.gz with paths like /home/gene.vcf.tar.gz
    :param file:
    :return:
    """
    time_stamp = datetime.now().date()

    # 1st remove path like /home/
    path_file = file.split("/")
    # 2nd removes file formats
    file_ = path_file[len(path_file)-1].split(".", 1)
    path_file.pop()
    # 3rd add time_stamp
    file_[0] = str(file_[0])+"_"+str(time_stamp)
    # 4th all is back together
    file = '.'.join(map(str, file_))

    path_file.append(file)
    file = '/'.join(map(str, path_file))
    print(file)
    return file