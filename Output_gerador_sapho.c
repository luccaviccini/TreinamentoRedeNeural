void inverte() {
float id0[97]; float id1[97]; float id2[97]; 
id0[0] = 1.0;id0[1] = 0.0;id0[2] = 0.0;
 id1[0] = 0.0;id1[1] = 1.0;id1[2] = 0.0;
 id2[0] = 0.0;id2[1] = 0.0;id2[2] = 1.0;

int i; size = 3;
float aux[97];  float auxid[97];
aux[0] = 0; aux[1] = 0; aux[2] = 0; 
auxid[0] = 0; auxid[1] = 0; auxid[2] = 0; 
/////////////////////////  pivo soma_0 /////////////////////////
/////////////////////////  CHECAGEM 0 /////////////////////////
    if ((soma_0[0] == 0)) {
        if(soma_1[0] != 0) {
            i = 0;
            while (i < size) {
                aux[i] = soma_0[i];
                auxid[i] = id0[i];
                soma_0[i] = soma_1[i];
                id0[i] = id1[i];
                soma_1[i] = aux[i];
                id1[i] = auxid[i];
                i = i + 1;} }
        else if(soma_2[0] != 0) {
            i = 0;
            while (i < size) {
                aux[i] = soma_0[i];
                auxid[i] = id0[i];
                soma_0[i] = soma_2[i];
                id0[i] = id2[i];
                soma_2[i] = aux[i];
                id2[i] = auxid[i];
                i = i + 1; } } } 
///////////////////////////  FIM CHECAGEM PIVO0 ////////////////////////////
    pivo = soma_0[0];
    i=0;
    while(i < size){
        soma_0[i] = soma_0[i]/pivo;
        id0[i] = id0[i]/pivo;
        i = i + 1;}
    i=0;
    cofator = soma_1[0];
    while (i<size) {
        soma_1[i] = soma_1[i] - cofator*soma_0[i];
        id1[i] = id1[i] - cofator*id0[i];
        i = i + 1; }
    i=0;
    cofator = soma_2[0];
    while (i<size) {
        soma_2[i] = soma_2[i] - cofator*soma_0[i];
        id2[i] = id2[i] - cofator*id0[i];
        i = i + 1; }
aux[0] = 0; aux[1] = 0; aux[2] = 0; 
auxid[0] = 0; auxid[1] = 0; auxid[2] = 0; 
/////////////////////////  pivo soma_1 /////////////////////////
/////////////////////////  CHECAGEM 1 /////////////////////////
    if ((soma_1[1] == 0)) {
        if(soma_2[1] != 0) {
            i = 0;
            while (i < size) {
                aux[i] = soma_1[i];
                auxid[i] = id1[i];
                soma_1[i] = soma_2[i];
                id1[i] = id2[i];
                soma_2[i] = aux[i];
                id2[i] = auxid[i];
                i = i + 1;} }
///////////////////////////  FIM CHECAGEM PIVO1 ////////////////////////////
    pivo = soma_1[1];
    i=0;
    while(i < size){
        soma_1[i] = soma_1[i]/pivo;
        id1[i] = id1[i]/pivo;
        i = i + 1;}
    i=0;
    cofator = soma_0[1];
    while (i<size) {
        soma_0[i] = soma_0[i] - cofator*soma_1[i];
        id0[i] = id0[i] - cofator*id1[i];
        i = i + 1; }
    i=0;
    cofator = soma_2[1];
    while (i<size) {
        soma_2[i] = soma_2[i] - cofator*soma_1[i];
        id2[i] = id2[i] - cofator*id1[i];
        i = i + 1; }
aux[0] = 0; aux[1] = 0; aux[2] = 0; 
auxid[0] = 0; auxid[1] = 0; auxid[2] = 0; 
/////////////////////////  pivo soma_2 /////////////////////////
    pivo = soma_2[2];
    i=0;
    while(i < size){
        soma_2[i] = soma_2[i]/pivo;
        id2[i] = id2[i]/pivo;
        i = i + 1;}
    i=0;
    cofator = soma_0[2];
    while (i<size) {
        soma_0[i] = soma_0[i] - cofator*soma_2[i];
        id0[i] = id0[i] - cofator*id2[i];
        i = i + 1; }
    i=0;
    cofator = soma_1[2];
    while (i<size) {
        soma_1[i] = soma_1[i] - cofator*soma_2[i];
        id1[i] = id1[i] - cofator*id2[i];
        i = i + 1; }


inverte();