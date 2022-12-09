CREATE TABLE classe (
    ref_g VARCHAR(15),
    intitule VARCHAR(50),
    niveau VARCHAR(15),
    filiere VARCHAR(15),
    PRIMARY KEY (ref_g)
);



CREATE TABLE Groupe (
    ref_c  VARCHAR(15),
    intitule VARCHAR(50),
    niveau VARCHAR(15),
    filiere VARCHAR(15)
    PRIMARY KEY (ref_c)

);

CREATE TABLE est_membre(
    ref_id_groupe VARCHAR(15),
    ref_id_classe VARCHAR(15),
    
    PRIMARY KEY (ref_id_eleve,ref_id_classe),
    FOREIGN KEY (ref_id_eleve) REFERENCES Groupe(ref_c),
    FOREIGN KEY (ref_id_classe) REFERENCES classe(ref_g));

