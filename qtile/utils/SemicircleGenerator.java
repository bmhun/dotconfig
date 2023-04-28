import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class SemicircleGenerator {
    public static void main(String[] args) throws Exception {
        String hexValue = "272727"; // your hex value goes here
        int[] c = components(from_hex("#" + hexValue));
        BufferedImage[] halves = getHalves(2048, 2048, new Color(c[0], c[1], c[2], 255));
        File outfileLeft = new File(new File(System.getProperty("user.home")), ".config/qtile/icons/sep_left_" + hexValue + ".png");
        File outfileRight = new File(new File(System.getProperty("user.home")), ".config/qtile/icons/sep_right_" + hexValue + ".png");

        ImageIO.write(halves[0], "png", outfileLeft);
        ImageIO.write(halves[1], "png", outfileRight);

    }

    /**
     * Splitting the circle in half
     */
    public static BufferedImage[] getHalves(int width, int height, Color c) {
        BufferedImage circle = getCircle(width, height, c);

        BufferedImage left = new BufferedImage(width / 2, height, circle.getType());
        for (int x = 0; x < left.getWidth(); x++) {
            for (int y = 0; y < left.getHeight(); y++) {
                left.setRGB(x, y, circle.getRGB(x, y));
            }
        }

        BufferedImage right = new BufferedImage(width / 2, height, circle.getType());
        for (int x = 0; x < right.getWidth(); x++) {
            for (int y = 0; y < right.getHeight(); y++) {
                right.setRGB(x, y, circle.getRGB(width / 2 + x, y));
            }
        }

        return new BufferedImage[] {left, right};
    }

    /**
     * Creating the circle
     */
    public static BufferedImage getCircle(int width, int height, Color c) {
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
        Graphics g = image.getGraphics();
        g.setColor(c);
        g.fillOval(0, 0, width, height);
        return image;
    }

    /**
     * Method from <a href="https://github.com/bmhun/javalib">my library</a>
     */
    public static int from_hex(String hex) {
        hex = hex.replaceAll("#", "");
        return switch (hex.length()) {
            case 3 -> rgb(
                    Integer.valueOf(hex.substring(0, 1).repeat(2), 16),
                    Integer.valueOf(hex.substring(1, 2).repeat(2), 16),
                    Integer.valueOf(hex.substring(2, 3).repeat(2), 16));
            case 6 -> rgb(
                    Integer.valueOf(hex.substring(0, 2), 16),
                    Integer.valueOf(hex.substring(2, 4), 16),
                    Integer.valueOf(hex.substring(4, 6), 16));
            case 4 -> argb(
                    Integer.valueOf(hex.substring(3, 4).repeat(2), 16),
                    Integer.valueOf(hex.substring(0, 1).repeat(2), 16),
                    Integer.valueOf(hex.substring(1, 2).repeat(2), 16),
                    Integer.valueOf(hex.substring(2, 3).repeat(2), 16));
            case 8 -> argb(
                    Integer.valueOf(hex.substring(6, 8), 16),
                    Integer.valueOf(hex.substring(0, 2), 16),
                    Integer.valueOf(hex.substring(2, 4), 16),
                    Integer.valueOf(hex.substring(4, 6), 16));
            default -> 0;
        };
    }

    /**
     * Method from <a href="https://github.com/bmhun/javalib">my library</a>
     */
    public static int[] components(int rgb) {
        int red = (rgb >> 16) & 0xff;
        int green = (rgb >> 8) & 0xff;
        int blue = (rgb) & 0xff;
        return new int[] {red, green, blue};
    }

    /**
     * Method from <a href="https://github.com/bmhun/javalib">my library</a>
     */
    public static int rgb(int... c) {
        int l = c.length;
        int red = l > 0 ? c[0] : 0;
        int green = l > 1 ? c[1] : 0;
        int blue = l > 2 ? c[2] : 0;
        return (red << 16) + (green << 8) + blue;
    }

    /**
     * Method from <a href="https://github.com/bmhun/javalib">my library</a>
     */
    public static int argb(int... c) {
        int l = c.length;
        int alpha = l > 0 ? c[0] : 255;
        int red = l > 1 ? c[1] : 0;
        int green = l > 2 ? c[2] : 0;
        int blue = l > 3 ? c[3] : 0;
        return (alpha << 24) + (red << 16) + (green << 8) + blue;
    }
}
