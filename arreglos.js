const ages=[5,16,9,52,17,23,11,69,27,40,16,18]
var nonCuad=[]
sumaPar=0
for(i=0;i<ages.length;i++){
    if(ages[i]%2==0){
        sumaPar=sumaPar+ages[i]
    }
    else{
        nonCuad[i]=ages[i]
        console.log(nonCuad[i])
    }
}
console.log(sumaPar)
