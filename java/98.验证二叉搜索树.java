/*
 * @lc app=leetcode.cn id=98 lang=java
 *
 * [98] 验证二叉搜索树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//  方法一：利用树的中序遍历来判断元素是否顺序排列，从而判断是否是二叉搜索树。 
class Solution {
    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        List list = new ArrayList();
        inOrder(root, list);
        for(int i=1; i<list.size(); i++){
            if((int)list.get(i-1) >= (int)list.get(i)){
                return false;
            }
        }
        return true;
    }

    public void inOrder(TreeNode root, List list){
        if(root == null) return;
        inOrder(root.left, list);
        list.add(root.val);
        inOrder(root.right, list);
    }
}
// @lc code=end

