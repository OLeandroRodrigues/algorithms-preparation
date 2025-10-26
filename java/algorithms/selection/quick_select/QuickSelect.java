package selection;
import java.util.Random;

public class QuickSelect {

    private static final Random random = new Random();

    public static int quickSelect(int[] arr, int low, int high, int k) {
        if (k < 1 || k > (high - low + 1)) {
            throw new IndexOutOfBoundsException("k out of range");
        }

        if (low == high) {
            return arr[low];
        }

        if (low < high) {
            int pivotIndex = random.nextInt(high - low + 1) + low; // random index between low and high
            swap(arr, pivotIndex, high);

            int p = partition(arr, low, high);
            int pos = p - low + 1;

            if (pos == k) {
                return arr[p];
            } else if (pos > k) {
                return quickSelect(arr, low, p - 1, k);
            } else {
                return quickSelect(arr, p + 1, high, k - pos);
            }
        }

        throw new IllegalStateException("Unexpected state in quickSelect");
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Example usage
    public static void main(String[] args) {
        int[] nums = {7, 10, 4, 3, 20, 15};
        int k = 3;
        int result = quickSelect(nums, 0, nums.length - 1, k);
        System.out.println(k + "-th smallest element is " + result);
    }
}