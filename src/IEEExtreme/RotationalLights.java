package IEEExtreme;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class RotationalLights {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        long n = readLong();
        long t = readLong();
        ArrayList<Long[]> validLightsOn = new ArrayList<>();
        Long[] currentLightsOn = new Long[(int) n];

        for(int i = 0; i < n; i++) {
            long light = readLong();
            currentLightsOn[i] = light;
        }

        validLightsOn.add(currentLightsOn.clone());
        ArrayList<String> rotations = new ArrayList<>();

        for(int i = 1; i < t; i++) {
            rotations.add(Integer.toString(i));
        }

        Long[] currentValidLights;
        int rotationsSize = rotations.size();
        boolean dupe = false;
        for(int i = 1; i < rotationsSize + 1; i++) {
            if(rotations.contains(Integer.toString(i))) {
                for(int j = 0; j < currentLightsOn.length; j++) {
                    currentLightsOn[j] = (currentLightsOn[j] + 1) % t;
                }

                for(int k = 0; k < validLightsOn.size(); k++) {
                    currentValidLights = validLightsOn.get(k);

                    if(compareArrays(currentValidLights, currentLightsOn)) {
                        removeDupes(i, t, rotations);
                        dupe = true;
                        break;
                    }
                }

                if(!dupe) {
                    validLightsOn.add(currentLightsOn.clone());
                }

                dupe = false;
            }
        }

        System.out.println(rotations.size());
    }

    public static boolean compareArrays(Long[] arr1, Long[] arr2) {
        HashSet<Long> set1 = new HashSet<Long>(Arrays.asList(arr1));
        HashSet<Long> set2 = new HashSet<Long>(Arrays.asList(arr2));
        return set1.equals(set2);
    }

    private static void removeDupes(long r, long t, ArrayList<String> l) {
        for(int i = 1; i <= t / r; i++) {
            l.remove(Long.toString(r * i));
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
