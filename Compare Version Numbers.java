public class Solution {
    public  int compareVersion(String version1, String version2) {
        if (version1 == null && version2 == null) {
            return 0;
        }
        if (version1 != null && version2 == null) {
            return 1;
        }
        if (version1 == null && version2 != null) {
            return -1;
        }
        List<Integer> l1 = parseVersion(version1);
        List<Integer> l2 = parseVersion(version2);

        for (int i = 0; i < Math.min(l1.size(), l2.size()); i++) {
            if (compare(l1.get(i), l2.get(i)) != 0) {
                return compare(l1.get(i), l2.get(i));
            }
        }
        if (l1.size() > l2.size()) {
            return 1;
        }
        if (l1.size() < l2.size()) {
            return -1;
        }
        return 0;
    }

    private static int compare(int x, int y) {
        if (x == y) {
            return 0;
        } else if (x > y) {
            return 1;
        } else {
            return -1;
        }
    }

    private static List<Integer> parseVersion(String v) {
        String[] ar = v.split("\\.");
        int pos = -1;
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < ar.length; i++) {
            int x = toInt(ar[ar.length - i - 1]);
            if (x != 0) {
                pos = i;
                break;
            }
        }
        if (pos == -1) {
            return list;
        }
        for (int i = 0; i < ar.length - pos; i++) {
            int x = toInt(ar[i]);
            list.add(x);
        }
        return list;
    }

    private static int toInt(String str) {
        if (str == null) {
            return 0;
        }
        try {
            return Integer.parseInt(str);
        } catch (NumberFormatException nfe) {
            return 0;
        }
    }
}