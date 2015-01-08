import subprocess
import sys
ex = '/home/fearofchou/Tools/Recsys/libFM/bin/'
def CT(BS_file):
    co = ex + 'convert'
    fi = ' --ifile ' + BS_file
    fox = ' --ofilex ' + BS_file + '.x'
    foy = ' --ofiley ' + BS_file + '.y'
    subprocess.call(co + fi + fox + foy,shell = True)

    tr = ex + 'transpose'
    fi = ' --ifile ' + BS_file + '.x'
    fo = ' --ofile ' + BS_file + '.xt'
    subprocess.call(tr + fi + fo,shell = True)



if __name__ == '__main__':
    convert_Transpose(sys.argv[1])
