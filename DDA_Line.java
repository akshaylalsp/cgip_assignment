import java.awt.*;
import javax.swing.*;

public class DDA_Line extends JPanel {

    private void drawLineDDA(Graphics g, int x1, int y1, int x2, int y2) {
        int dx = x2 - x1;
        int dy = y2 - y1;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));

        float xIncrement = (float) dx / steps;
        float yIncrement = (float) dy / steps;

        float x = x1;
        float y = y1;

        for (int i = 0; i <= steps; i++) {
            g.fillRect(Math.round(x), Math.round(y), 1, 1);
            x += xIncrement;
            y += yIncrement;
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawLineDDA(g, 50, 50, 200, 150); // Example line coordinates (x1, y1, x2, y2)
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("DDA Line Drawing Algorithm");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setLocationRelativeTo(null);
        frame.add(new DDA_Line());
        frame.setVisible(true);
    }
}
