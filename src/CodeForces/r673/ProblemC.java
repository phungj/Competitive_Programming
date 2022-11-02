package CodeForces.r673;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class ProblemC {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int t = readInt();
        int n;
        int[] a;
        int[][] k2D;

        for (int i = 0; i < t; i++) {
            n = readInt();
            a = new int[n];

            for (int j = 0; j < n; j++) {
                a[j] = readInt();
            }

            for (int k = 1; k <= n; k++) {
                k2D = k2DGen(a, k);
                if (k == n) {
                    System.out.println(k2DCheck(k2D, k));
                }

                else {
                    System.out.print(k2DCheck(k2D, k) + " ");
                }
            }
        }
    }

    private static int getMin(ArrayList<Integer> l) {
        int min = Integer.MAX_VALUE;
        int currentVal;

        for (int i = 0; i < l.size(); i++) {
            currentVal = l.get(i);
            if (currentVal < min) {
                min = currentVal;
            }
        }

        return min;
    }

    private static int[][] k2DGen(int[] a, int s) {
        int firstIndex = 0;
        int secondIndex = firstIndex + s;
        int[][] k2D = new int[a.length - s + 1][s];

        while (secondIndex <= a.length) {
            for (int i = 0; i < k2D.length; i++) {
                for (int j = 0; j < k2D[0].length; j++) {
                    k2D[i][j] = a[j + firstIndex];
                }
            }

            firstIndex++;
            secondIndex++;
        }

        return k2D;
    }

    private static int k2DCheck(int[][] k2D, int s) {
        int currentRow = 0;
        int currentCol = 0;
        int currentVal = k2D[currentRow][currentCol];
        boolean notK = true;
        ArrayList<Integer> validKs = new ArrayList<Integer>();

        while (currentRow < k2D.length) {
            for (int k = 0; k < validKs.size(); k++) {
                if (validKs.contains(currentVal)) {
                    if (currentCol == k2D.length - 1 && currentRow != k2D.length - 1) {
                        currentRow++;
                        currentCol = 0;
                    } else {
                        currentCol++;
                    }
                }

                for (int i = currentRow + 1; i < k2D.length; i++) {
                    notK = true;
                    for (int j = 0; j < k2D[0].length; j++) {
                        if (currentVal == k2D[i][j]) {
                            notK = false;
                        }
                    }

                    if (notK == true) {
                        break;
                    }
                }

                if (notK == false) {
                    validKs.add(currentVal);
                }

                if (currentCol == k2D.length - 1 && currentRow != k2D.length - 1) {
                    currentRow++;
                    currentCol = 0;
                } else {
                    currentCol++;
                }
            }
        }

        if(validKs.isEmpty()) {
            return -1;
        }

        else {
            return getMin(validKs);
        }
    }

    private static final int SPACE_INT = ' ';
    private static final int ZERO_INT = '0';
    private static final int NL_INT = '\n';
    @SuppressWarnings("DuplicatedCode")
    private static int readInt() throws IOException {
        int ret = br.read();
        while (ret <= SPACE_INT) {
            ret = br.read();
        }
        final boolean neg = ret == '-';
        if (neg) {
            ret = br.read();
        }
        ret -= ZERO_INT;
        int read = br.read();
        while (read >= ZERO_INT) {
            ret *= 10;
            ret += read - ZERO_INT;
            read = br.read();
        }
        while (read <= SPACE_INT && read != -1 && read != NL_INT) {
            br.mark(1);
            read = br.read();
        }
        if (read > SPACE_INT) {
            br.reset();
        }
        return neg ? -ret : ret;
    }
    @SuppressWarnings("DuplicatedCode")
    private static long readLong() throws IOException {
        long ret = br.read();
        while (ret <= SPACE_INT) {
            ret = br.read();
        }
        final boolean neg = ret == '-';
        if (neg) {
            ret = br.read();
        }
        ret -= ZERO_INT;
        int read = br.read();
        while (read >= ZERO_INT) {
            ret *= 10;
            ret += read - ZERO_INT;
            read = br.read();
        }
        while (read <= SPACE_INT && read != -1 && read != NL_INT) {
            br.mark(1);
            read = br.read();
        }
        if (read > SPACE_INT) {
            br.reset();
        }
        return neg ? -ret : ret;
    }
    @SuppressWarnings("DuplicatedCode")
    private static String readWord() throws IOException {
        int ret = br.read();
        while (ret <= SPACE_INT && ret != -1) {
            ret = br.read();
        }
        if (ret == -1) {
            return "";
        }
        char[] cb = new char[32];
        int idx = 0;
        while (ret > SPACE_INT) {
            if (idx == cb.length) {
                char[] ncb = new char[cb.length * 2];
                System.arraycopy(cb, 0, ncb, 0, cb.length);
                cb = ncb;
            }
            cb[idx++] = (char)ret;
            ret = br.read();
        }
        while (ret <= SPACE_INT && ret != -1 && ret != NL_INT) {
            br.mark(1);
            ret = br.read();
        }
        if (ret > SPACE_INT) {
            br.reset();
        }
        return new String(cb, 0, idx);
    }
}
