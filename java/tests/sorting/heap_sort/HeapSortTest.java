package sorting;
import java.util.List;
import java.util.Arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class HeapSortTest {

    @Test
    public void testSortAscBasic() {
        List<Integer> input = Arrays.asList(4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1);
        List<Integer> expected = Arrays.asList(1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100);

        List<Integer> result = HeapSort.sortAsc(input);
        assertEquals(expected, result);
    }

    @Test
    public void testSortDescBasic() {
        List<Integer> input = Arrays.asList(4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1);
        List<Integer> expected = Arrays.asList(100, 50, 30, 10, 10, 8, 5, 5, 4, 2, 1);

        List<Integer> result = HeapSort.sortDesc(input);
        assertEquals(expected, result);
    }

    @Test
    public void testEmptyList() {
        List<Integer> input = List.of();
        List<Integer> expected = List.of();

        assertEquals(expected, HeapSort.sortAsc(input));
        assertEquals(expected, HeapSort.sortDesc(input));
    }

    @Test
    public void testSingleElementList() {
        List<Integer> input = List.of(42);
        List<Integer> expectedAsc = List.of(42);
        List<Integer> expectedDesc = List.of(42);

        assertEquals(expectedAsc, HeapSort.sortAsc(input));
        assertEquals(expectedDesc, HeapSort.sortDesc(input));
    }

    @Test
    public void testAllEqualElements() {
        List<Integer> input = Arrays.asList(7, 7, 7, 7, 7);
        List<Integer> expected = Arrays.asList(7, 7, 7, 7, 7);

        assertEquals(expected, HeapSort.sortAsc(input));
        assertEquals(expected, HeapSort.sortDesc(input));
    }
}