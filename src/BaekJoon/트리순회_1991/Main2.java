package BaekJoon.트리순회_1991;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main2 {
    static class Node{
        char data;
        Node left;
        Node right;

        public Node(char data) {
            this.data = data;
        }
    }

    static class Tree{
        Node root;

        public void createNode(char data, char left, char right) {
            if (root == null) {
                root = new Node(data);
                root.left = new Node(left);
                root.right = new Node(right);
            } else {
                searchNode(root, data, left, right);
            }
        }

        public void searchNode(Node root, char data, char left, char right) {
            if (root == null) {
                return;
            } else if (root.data == data) {
                root.left = new Node(left);
                root.right = new Node(right);
            } else {
                searchNode(root.left, data, left, right);
                searchNode(root.right, data, left, right);
            }
        }

        public void preorder(Node root) {
            // 루트 왼 오
            System.out.println(root.data);
            if (root.left.data != '.')
                preorder(root.left);
            if (root.right.data != '.')
                preorder(root.right);
        }

        public void inorder(Node root) {
            if (root.left.data != '.')
                inorder(root.left);
            System.out.println(root.data);
            if (root.right.data != '.')
                inorder(root.right);
        }

        public void postorder(Node root) {
            if (root.left.data != '.')
                postorder(root.left);
            if (root.right.data != '.')
                postorder(root.right);
            System.out.println(root.data);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Main.Tree tree = new Main.Tree();
        for (int i = 0; i < n; i++) {
            char[] s = br.readLine().replaceAll(" ", "").toCharArray();
            tree.createNode(s[0], s[1], s[2]);
        }

        tree.preorder(tree.root);
        System.out.println();

        tree.inorder(tree.root);
        System.out.println();

        tree.postorder(tree.root);
        System.out.println();
    }
}
