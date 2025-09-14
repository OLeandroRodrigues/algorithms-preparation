namespace Algorithms.Sorting;

public static class MergeSort
{
    public static int[] Sort(int[] arr)
    {
        if(arr == null || arr.Length <= 1){
			return arr;
		}
		
		int mid = arr.Length / 2;
        int[] L = new int[mid];
        int[] R = new int[arr.Length - mid];

        Array.Copy(arr, 0, L, 0, mid);
        Array.Copy(arr, mid, R, 0, arr.Length - mid);
		
		Sort(L);
		Sort(R);
		
		int i = 0, j = 0, k = 0;
		
		while(i < L.Length && j < R.Length){
			if(L[i] <= R[j]){
				arr[k] = L[i];
				i += 1;
			}else{
				arr[k] = R[j];
				j += 1;
			}
			k += 1;
			
		}
		
		while(i < L.Length){
			arr[k] = L[i];
			i += 1;
			k += 1;
		}
		
		while(j < R.Length){
			arr[k] = R[j];
			j += 1;
			k += 1;
		}
		
		return arr;
    }
}