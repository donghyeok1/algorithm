<%@page import="java.sql.*"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
        <%
                Connection conn = null;
                ResultSet rs = null;

                String url = "jdbc:mysql://192.168.214.50:3306/good?serverTimezone=UTC";
                String id = "admin";
                String pwd = "qwer1234";


                try {
                        Class.forName("com.mysql.jdbc.Driver");
                        conn = DriverManager.getConnection(url, id, pwd);
                        Statement stmt = conn.createStatement();


                        String sql = "SELECT * FROM product";
                        rs = stmt.executeQuery(sql);

                        String result = "[";


                        while(rs.next()) {
                                result += "{";
                                result += "\"name\":\""+rs.getString("name")+"\"";
                                result += ", \"img_url\":\""+rs.getString("img_url") +"\"";
                                result += ", \"price\":\""+rs.getString("price")+"\"";
                                result += "},";
                        }
                        result = result.substring(0, result.length() - 1);
                        result += "]";
                        out.println(result);

                        conn.close();
                } catch (Exception e) {

                        e.printStackTrace();
                }
        %>
