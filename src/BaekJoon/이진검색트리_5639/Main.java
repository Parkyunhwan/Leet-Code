package BaekJoon.이진검색트리_5639;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 이진 검색 트리
// 전위 순회는 루트부터 왼쪽아랫단계로 트리를 순회한다. 이를 이용해 트리를 재구성할 수 있다. (재귀)
// 재구성된 트리를 이용해 후위순회를 구할 수 있었다.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Tree tree = new Tree(new Node(Integer.parseInt(br.readLine())));
        while(true) {
            String s = br.readLine();
            if (s == null || "".equals(s)) {
                break;
            }
            tree.insert(tree.root, Integer.parseInt(s));
        }

        tree.postOrder(tree.root);
    }

    static class Tree {
        Node root;

        public Tree(Node node) {
            this.root = node;
        }

        public void insert(Node currNode, int insertData) {
            if (currNode.data > insertData) {
                if (currNode.left == null)
                    currNode.left = new Node(insertData);
                else
                    insert(currNode.left, insertData);
            } else {
                if (currNode.right == null)
                    currNode.right = new Node(insertData);
                else
                    insert(currNode.right, insertData);
            }
        }

        public void postOrder(Node node) {
            if (node == null)
                return ;
            postOrder(node.left);
            postOrder(node.right);
            System.out.println(node.data);
        }
    }

    static class Node {
        Node left;
        Node right;
        int data;

        public Node(int data) {
            this.data = data;
        }

        public Node(Node left, Node right, int data) {
            this.left = left;
            this.right = right;
            this.data = data;
        }
    }
}
