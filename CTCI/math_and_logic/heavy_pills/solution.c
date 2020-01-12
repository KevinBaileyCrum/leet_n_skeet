// given 20 pill bottles filled with pills s.t.
// 19 bottles have pills weighing 1g and 1 bottle weighing 1.1g
// given a scale that records exact weight determine which bottle has the heavy pill
//
// you may only read from the scale exactly once
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct PillBottle {
  double weight;
} PillBottle;

int heavyBottleFinder(PillBottle P[], int numBottles){
  double euclid = (numBottles) * (numBottles + 1) / 2;
  double scale = 0.0;
  for(int i=0; i<numBottles; i++){
    scale += P[i].weight * (i+1); // off by one
  }
  return ((scale - euclid) * 10) - 1;
}

int main(){
  PillBottle P[20];
  srand(time(NULL));
  int heavyBottle = rand()%20; // generate 0 - 19
  
  for(int i=0; i<20; i++){
    if(i == heavyBottle)
      P[i].weight = 1.1;
    else
      P[i].weight = 1.0;
  }
 
  if(heavyBottleFinder(P, 20) == heavyBottle)
    printf("success");
  for(int i=0; i<20; i++)
    printf("%d %f\n",i ,P[i].weight);

}
