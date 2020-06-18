// globals
int i = 0; //iterator for array-making loop
int j = 0; //iterator for presort array-displaying loop
//int k = 0; //iterator for postsort array-displaying loop
int x = 1; //iterator 1 for sort algorithm
int y = 0; //iterator 2 for sort algorithm
int hlLine = -1; //y-value of a highlighted line
int[] lineHeights = new int[800]; //array of y-values for each line
boolean started = false;


void setup(){
  size(800,400);
  frameRate(240);
  background(232, 232, 232);
}

void draw(){

  if(!started){
   textSize(26);
   fill(0);
   textAlign(CENTER);
   text("Click to start",400,200);
   return;
  }

  if(i < lineHeights.length){
    if(i == 0){
      textSize(26);
      fill(0);
      textAlign(CENTER);
      text("Filling the array...",400,200);
    }

    lineHeights[i] = (int)(random(0,400));
    i++;

    if(i == 800){
      background(232, 232, 232);
    }
  }
  else{
    if(j < lineHeights.length){
      line(j,400,j,lineHeights[j]);
      j++;
    }
    else{

      int n = lineHeights.length;
      if(x<n){
        int key = lineHeights[x];
        int y = x-1;

        /* Move elements of arr[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
        while (y>=0 && lineHeights[y] > key){

          resetHighlight();

          lineHeights[y+1] = lineHeights[y];
          stroke(232, 232, 232);
          line(y,0,y,400);
          line(y+1,0,y+1,400);

          //show highlighted first (red line)
          stroke(0);
          line(y,400,y,lineHeights[y]);

          stroke(0);
          line(y+1,400,y+1,lineHeights[y+1]);

          //bring back to normal (black line)
          /*
          stroke(0);
          line(y,400,y,lineHeights[y]); //before
          line(y+1,400,y+1,lineHeights[y+1]);
          */

          y = y-1;
          stroke(232, 232, 232);
          line(y-1,0,y-1,400);
          if(y > 0){
            //show highlighted first (red line)
            /*
            stroke(0);
            line(y-1,400,y-1,lineHeights[y-1]);
            */

            //bring back to normal (black line)
            stroke(0,x,y);
            hlLine = y-1; //store the value of the highlighted line
            line(y-1,400,y-1,lineHeights[y-1]);
          }

        }

        lineHeights[y+1] = key;
        x++;
      }else{
         resetHighlight();
      }
    }
  }
}

void resetHighlight(){
  //If a line was previously highlighted, re-color as black
  if(hlLine > -1){
    stroke(0);
    line(hlLine,400,hlLine,lineHeights[hlLine]);

    hlLine = -1;
  }
}


//i -> x
//j -> y
//the following is code for Insertion Sort
void mySort(int arr[]){
  int n = arr.length;
  for (int x=1; x<n; ++x){
    int key = arr[x];
    int y = x-1;

    /* Move elements of arr[0..i-1], that are
    greater than key, to one position ahead
    of their current position */
    while (y>=0 && arr[y] > key){
      arr[y+1] = arr[y];
      stroke(232, 232, 232);
      line(y,0,y,400);
      line(y+1,0,y+1,400);
      stroke(0);
      line(y,400,y,lineHeights[y]);
      line(y+1,400,y+1,lineHeights[y+1]);
      y = y-1;
      stroke(232, 232, 232);
      line(y-1,0,y-1,400);
      stroke(0);
      if(y > 0){
        line(y-1,400,y-1,lineHeights[y-1]);
      }

    }
  arr[y+1] = key;
  }

}

void mouseClicked(){
  if(!started){
    started=  true;
    background(232, 232, 232);
  }
}
