# # Example of Terraform and Helm to deploy Nginx Ingress controller to K8s cluster 
# # Class = external-nginx
resource "helm_release" "external_nginx" {
  name = "external"

  repository       = "https://kubernetes.github.io/ingress-nginx"
  chart            = "ingress-nginx"
  namespace        = "ingress"
  create_namespace = true
  version          = "4.7.1"

  set {
    name  = "controller.image.tag"
    value = "v1.6.4"
  }

  set {
    name  = "controller.ingressClassResource.name"
    value = "external-nginx"
  }
}
