public class Product {
    private Long id;
    private String name;
    private double price;

    // Constructor, Getters y Setters
    public Product(Long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
    public double getPrice() { return price; }
}mport org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

@Service
public class CartService {
    private List<Product> items = new ArrayList<>();

    public void addProduct(Product product) {
        items.add(product);
    }

    public double getTotal() {
        return items.stream()
                    .mapToDouble(Product::getPrice)
                    .sum();
    }

    public List<Product> getItems() {
        return items;
    }
}import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/cart")
public class CartController {

    private final CartService cartService;

    public CartController(CartService cartService) {
        this.cartService = cartService;
    }

    @PostMapping("/add")
    public String addToCart(@RequestBody Product product) {
        cartService.addProduct(product);
        return "Producto añadido: " + product.getName();
    }

    @GetMapping("/total")
    public String checkout() {
        double total = cartService.getTotal();
        return "El total de tu compra es: $" + total;
    }
}