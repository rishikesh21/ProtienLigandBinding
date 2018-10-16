from main.readPDBfiles import read_pdb;

if __name__ == '__main__':
    X_list_lig, Y_list_lig, Z_list_lig, atomtype_list_lig = read_pdb("/Users/mac/Downloads/CS5242/Project/training_data/2061_lig_cg.pdb")
    X_list_pro, Y_list_pro, Z_list_pro, atomtype_list_pro = read_pdb("/Users/mac/Downloads/CS5242/Project/training_data/2061_pro_cg.pdb")


    print(X_list_lig)
    print(Y_list_lig)
    print(Z_list_lig)
    print(atomtype_list_lig)

    print(X_list_pro)
    print(Y_list_pro)
    print(Z_list_pro)
    print(atomtype_list_pro)
