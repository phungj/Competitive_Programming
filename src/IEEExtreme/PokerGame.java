package IEEExtreme;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class PokerGame {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int k = readInt();
        String community = readWord();
        String raises = readWord();
        int[] occurrences = new int[13];

        char currentCommunityCard, raised, currentPossibleCard;
        int currentCardIndex, currentCardOccurrences, handLength, remainingCardCount;
        int currentCardCount = 0;
        int index = 0;
        String possibleHand = "";
        String currentPossibleHand = "";
        String finalHand = "";
        String currentComponent;
        ArrayList<Character> possibleCards = new ArrayList<>();
        ArrayList<String> possibleHandComponents = new ArrayList<>();
        boolean added = false;

        for(int i = 2; i <= 9; i++) {
            possibleCards.add(Character.forDigit(i, 10));
        }

        possibleCards.add('X');
        possibleCards.add('J');
        possibleCards.add('Q');
        possibleCards.add('K');
        possibleCards.add('A');

        for(int i = 0; i < community.length(); i++) {
            currentCommunityCard = community.charAt(i);
            raised = raises.charAt(i);
            currentCardIndex = getCardIndex(currentCommunityCard);
            currentCardOccurrences = ++occurrences[currentCardIndex];

            if(currentCardOccurrences == 1 && raised == 'y') {
                if(possibleHand.length() == 0) {
                    possibleHand += currentCommunityCard;
                }

                else {
                    if(currentCommunityCard < possibleHand.charAt(0)) {
                        possibleHand = currentPossibleHand + possibleHand;
                    }

                    else {
                        for(int j = 0; j < possibleHand.length(); j++) {
                            if(possibleHand.charAt(j) > currentCommunityCard) {
                                possibleHand = possibleHand.substring(0, j) + currentCommunityCard + possibleHand.substring(j);
                                added = true;
                            }
                        }

                        if(!added) {
                            possibleHand += currentCommunityCard;
                            added = false;
                        }
                    }
                }
            }

            else {
                possibleCards.remove(String.valueOf(currentCommunityCard));
            }

            if(currentCardOccurrences == 2 && raised != 'y') {
                System.out.println("impossible");
                System.exit(0);
            }

            else if(currentCardOccurrences == 3 && raised != 'y') {
                System.out.println("impossible");
                System.exit(0);
            }

            else if(currentCardOccurrences == 4 && raised != 'y') {
                System.out.println("impossible");
                System.exit(0);
            }
        }

        handLength = possibleHand.length();

        if(handLength > k) {
            System.out.println("impossible");
        }

        else if(handLength == k) {
            System.out.println(possibleHand);
        }

        else {
            while(currentCardCount < k) {
                for(int i = 0; i < handLength; i++) {
                    possibleHandComponents.add(String.valueOf(possibleHand.charAt(i)));
                }

                for(int i = 0; i < possibleHandComponents.size(); i++) {
                    currentComponent =  possibleHandComponents.get(i);
                    currentCardCount += currentComponent.length();
                }

                remainingCardCount = k - currentCardCount;
                currentComponent = "";

                while(remainingCardCount > 0) {
                    currentPossibleCard = possibleHandComponents.get(index).charAt(0);
                    if(remainingCardCount >= 3) {
                        for(int i = 0; i < 4; i++) {
                            currentComponent += currentPossibleCard;
                        }
                        possibleHandComponents.set(index, currentComponent);
                        currentCardCount += 3;
                    }

                    else if(remainingCardCount < 3) {
                        for(int i = 0; i < remainingCardCount; i++) {
                            currentComponent += currentPossibleCard;
                        }

                        possibleHandComponents.set(index, currentComponent + currentPossibleCard);
                        currentCardCount += remainingCardCount;
                    }

                    remainingCardCount = k - currentCardCount;
                    index++;
                }
            }
        }

        for(int i = 0; i < possibleHandComponents.size(); i++) {
            finalHand += possibleHandComponents.get(i);
        }

        System.out.println(finalHand);
    }

    private static int getFaceLexicographicValue(char card) {
        switch(card) {
            case 'X':
                return 10;
            case 'J'
                return 11;
        }
    }

    private static int getCardIndex(char card) {
        switch(card) {
            case '2':
                return 0;

            case '3':
                return 1;

            case '4':
                return 2;

            case '5':
                return 3;

            case '6':
                return 4;

            case '7':
                return 5;

            case '8':
                return 6;

            case '9':
                return 7;

            case 'X':
                return 8;

            case 'J':
                return 9;

            case 'Q':
                return 10;

            case 'K':
                return 11;

            case 'A':
                return 12;

            default:
                return -1;
        }
    }

    private class Card {

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
