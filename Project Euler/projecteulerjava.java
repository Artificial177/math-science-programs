package projecteulerjava;
import java.math.BigInteger;

public class projecteulerjava {
	public static void main(String[] args) {
		BigInteger cut = BigInteger.valueOf(10).pow(10);
		BigInteger prime = BigInteger.valueOf(2)
				.modPow(BigInteger.valueOf(7830457), cut)
				.multiply(BigInteger.valueOf(28433))
				.add(BigInteger.ONE)
				.mod(cut);
		
		System.out.println(prime);
	}
}

