package sorting;

import java.util.Arrays;

public final class MergeSort{
    private MergeSort(){}

    public static int[] mergeSort(int[] arr){

        if(arr.length <= 1)
            return arr;
        

        int mid = arr.length / 2;
        int[] L = Arrays.copyOfRange(arr, 0, mid);
        int[] R = Arrays.copyOfRange(arr, mid, arr.length);

        mergeSort(L);
        mergeSort(R);

        int i = 0, j = 0, k = 0;

        while(i < L.length && j < R.length){
            if(L[i] <= R[j]){
                arr[k] = L[i];
                i += 1;
            }else{
                arr[k] = R[j];
                j += 1;
            }
            k += 1;
        }

        while(i < L.length){
            arr[k] = L[i];
            i += 1;
            k += 1;
        }
        
        while(j < R.length){
            arr[k] = R[j];
            j += 1;
            k += 1;
        }

        return arr;
    }
}